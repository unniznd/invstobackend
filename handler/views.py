from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

import pandas as pd

from handler.serializer import StockSerializer
from handler.models import Stock

class StockView(ListAPIView):
    serializer_class = StockSerializer
    query_set = Stock.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            bytedata = request.data['data'].read()
            failed = []
            with open('data.csv','wb') as f:
                f.write(bytedata)
                f.close()
            
            df = pd.read_csv('data.csv')
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        for index in df.index:
            try:
                stock = Stock(
                    datetime = df['datetime'][index],
                    close = df['close'][index],
                    high = df['high'][index],
                    low = df['low'][index],
                    volume = df['volume'][index],
                    open = df['open'][index],
                    instrument = df['instrument'][index]
                )
                stock.save()
            except:
                failed.append(index)
        if len(failed) == 0:
            return Response({"status":"successful"}, status=status.HTTP_201_CREATED)
        
        else:
            return Response(
                {"status":"unsuccessful","index":failed}, 
                status=status.HTTP_201_CREATED
            )
   
   
    def get(self, request, *args, **kwargs):
        query_set = Stock.objects.all()
        stock = StockSerializer(query_set, many=True)

        return Response(stock.data,status=status.HTTP_200_OK)
