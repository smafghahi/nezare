from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .rules import ComplianceRules


class OrderIngestAPIView(APIView):
    """
    API endpoint for ingesting orders
    """
    
    def post(self, request):
        """
        Handle POST requests to ingest orders
        """
        try:
            # Extract order data from request
            order_data = request.data
            
            # Validate order using compliance rules
            if not ComplianceRules.validate_order(order_data):
                return Response(
                    {'error': 'Order does not comply with rules'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Create order in database
            order = Order.objects.create(**order_data)
            
            return Response(
                {'message': 'Order ingested successfully', 'order_id': order.id}, 
                status=status.HTTP_201_CREATED
            )
        
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
