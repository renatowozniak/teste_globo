FROM node:18-alpine

WORKDIR /app

RUN npm install express

COPY index.js .

EXPOSE 5002

HEALTHCHECK --interval=10s --timeout=3s CMD wget --no-verbose --tries=1 --spider http://localhost:5002/texto || exit 1

CMD ["node", "index.js"]