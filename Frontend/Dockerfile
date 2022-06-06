FROM node:latest
RUN apt-get update
WORKDIR /app
COPY app/ .
RUN npm install
RUN npm install react-scripts@3.4.1 -g

CMD ["npm", "start"]
EXPOSE 3000
