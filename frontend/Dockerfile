# Use an official Node runtime as a parent image
FROM node:14

# Create and set the working directory for React
WORKDIR /app/frontend

# Copy the React files into the container
COPY . .

# Install dependencies
RUN npm install

# Expose the React development server port
EXPOSE 3000

# CMD to start React development server
CMD ["npm", "start"]