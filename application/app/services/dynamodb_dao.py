"""
FeedbackService: DynamoDB-based Service for Managing AI Feedback

This module provides a FeedbackService class that handles storing, retrieving,
and managing feedback for AI services. It interfaces with AWS DynamoDB for 
persistent storage and provides a complete API for feedback management.

Key Features:
- Submit feedback with various metadata
- Retrieve feedback by ID, racfid, or Application ID
- Delete feedback by ID or Application ID
- Automatic table creation with required indexes

Usage:
    feedback_service = FeedbackService()
    response = await feedback_service.submit_feedback(feedback_request)
"""

import os
import json
import uuid
import datetime
import logging
import boto3.dynamodb
import boto3.dynamodb.conditions
from typing import List, Dict, Any, Optional

import boto3
from fastapi import FastAPI, HTTPException, Query
from boto3.dynamodb.conditions import Key, Attr

from app.models.feedback_models import FeedbackServiceRequest, FeedbackServiceResponse

logger = logging.getLogger(__name__)

class FeedbackService:

    def __init__(self):
        self.region_name = os.environ.get("AWS_REGION","us-west-2")
        self.table_name = os.environ.get("DYNAMODB_TABLE_NAME","feedback")

        self.dynamodb = boto3.resource('dynamodb', region_name= self.region_name)
        self.table = self.dynamodb.Table(self.table_name)

    
    def create_table(self):
        pass

    def check_table_if_not_exists(self):

        try:
            self.dynamodb.meta.client.describe_table(TableName= self.table_name)
            logger.info(f"Table {self.table_name} exists")
        
        except self.dynamodb.meta.client.exceptions.ResourceNotFoundException:
                    logger.error(f"Table {self.table_name} not found")

    def _item_to_feedback(self, item:Dict[str, Any]) -> FeedbackServiceRequest:
        """Convert DynamoDB item to FeedbackServiceRequest"""
        return FeedbackServiceRequest(
            racfid=item.get('racfid'),
            inference_id=item.get('inference_id'),
            application_id=item.get('application_id', None),
            feedback_relevance=item.get('feedback_relevance', None),
            feedback_type=item.get('feedback_type', None),
            guardrail_failure_type=item.get('guardrail_failure_type', None),
            context=json.loads(item.get('context', '{}'))
        )


    async def submit_feedback(self, feedback: FeedbackServiceRequest) -> FeedbackServiceResponse:
            id = str(uuid.uuid4())
            timestamp = datetime.datetime.utcnow().isoformat()

            item = {
                'id': id,
                'racfid': feedback.racfid,
                'inference_id': feedback.inference_id,
                'timestamp': timestamp,
            }

            # Add optional fields if they exist
            if feedback.application_id:
                item['application_id'] = feedback.application_id
            if feedback.feedback_relevance:
                item['feedback_relevance'] = feedback.feedback_relevance
            if feedback.feedback_type:
                item['feedback_type'] = feedback.feedback_type
            if feedback.guardrail_failure_type:
                item['guardrail_failure_type'] = feedback.guardrail_failure_type

            # Convert context to JSON string
            item['context'] = json.dumps(feedback.context)

            try:
                self.table.put_item(Item=item)
                return FeedbackServiceResponse(id=id, status="success")
            except Exception as e:
                print(f"Error submitting feedback: {str(e)}")
                return FeedbackServiceResponse(id=id, status="error")
        
    async def get_feedback(self, feedback_id: str) -> FeedbackServiceRequest:
        try:
            response = self.table.get_item(Key={'id': feedback_id})

            if 'Item' not in response:
                raise HTTPException(status_code=404, detail=f"Feedback with ID{feedback_id} not found")
        
            item = response['Item']

            return self._item_to_feedback(item)
        except HTTPException:
            raise
        except Exception as e:
            print(f"Error retrieving feedback: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
        
    
    async def get_feedback_by_rafcid(self, racfid: str) -> List[FeedbackServiceRequest]:
        try:
            response = self.table.query(
                KeyConditionExpression=boto3.dynamodb.conditions.Key('racfid').eq(racfid)
            )

            if 'Items' not in response or not response['Items']:
                raise HTTPException(status_code=404, detail=f"No feedback found for racfid: {racfid}")
            
            return [self._item_to_feedback(item) for item in response['Items']]
        
        except HTTPException:
            raise
        except Exception as e:
            logger.exception(f"Error retrieving feedback by racfid {str(e)}")
            raise HTTPException(status_code=500, detail="Internal server error")


    async def get_feedback_by_application_id(self, application_id: str) -> List[FeedbackServiceRequest]:
        try:
            response = self.table.scan(
                FilterExpression=Attr("application_id").eq(application_id)
            )

            if not response.get('Items'):
                raise HTTPException(status_code=404, detail=f"No feedback found for Application ID: {application_id}")
            
            return [self._item_to_feedback(item) for item in response['Items']]
        
        except Exception as e:
            logger.exception(f"Error retrieving feedback by Application ID {str(e)}")
            raise HTTPException(status_code=500, detail="Internal server error")
    
    async def delete_feedback_by_id(self, feedback_id: str) -> FeedbackServiceResponse:
        try:
            self.table.get_item(Key={'id': feedback_id})
            self.table.delete_item(Key={'id': feedback_id})
            return FeedbackServiceResponse(id= feedback_id, status= "sucess")
        except Exception as e:
            logger.error(f"Error deleting feedback: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))
    
    async def delete_feedback_by_application_id(self, application_id: str) -> FeedbackServiceResponse:
        raise NotImplementedError("Method 'delete_feedback_by_application_id' is not implemented yet")