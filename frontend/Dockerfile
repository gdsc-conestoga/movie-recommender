FROM node:alpine 
WORKDIR /app
COPY package.json .
ENV PATH /app/node_modules/.bin:$PATH
COPY package-lock.json .
RUN npm install 
COPY . .
CMD ["npm", "start"]