FROM mongo:latest

WORKDIR /app

COPY . /app

EXPOSE 27017

CMD mongod && mongoimport -d "hotel" -c "booking" --file "/hotel_bookings.csv" --headerline
