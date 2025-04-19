# Stage 1: Build the frontend
FROM node:18 AS builder

# Set working directory
WORKDIR /app

# Copy required config and lock files
COPY package.json yarn.lock svelte.config.js vite.config.js ./

# Install dependencies
RUN yarn install

# Copy the rest of the source files
COPY . .

# Build the frontend
RUN yarn build

# Stage 2: Serve with Caddy
FROM caddy:2-alpine

# Set working directory
WORKDIR /usr/share/caddy

# Copy the build output from the previous stage
COPY --from=builder /app/dist /usr/share/caddy

CMD ["caddy", "file-server", "--root", "/usr/share/caddy", "--listen", ":80"]
