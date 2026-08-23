FROM node:latest

WORKDIR /frontend-with-react

COPY  public/  /frontend-with-react/public
COPY src/  /frontend-with-react/src
COPY package.json  /frontend-with-react
COPY vite.config.js  /frontend-with-react

RUN npm install

EXPOSE 5173

CMD ["npm","run","dev"]

#CMD ["npm", "start"]
