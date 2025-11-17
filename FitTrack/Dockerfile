FROM node:18-alpine
WORKDIR /usr/src/app

# Copy package files if present (keeps build cache usable)
COPY package*.json ./

# Install dependencies if package.json exists
RUN if [ -f package.json ]; then npm ci --only=production || true; fi

# Copy everything (project might be added later)
COPY . .

# Default command: print a helpful message (replace with real start command later)
CMD ["/bin/sh", "-c", "printf 'This is a placeholder Docker image for FitTrack. Add a start script in package.json to run the app.\n' && sleep 3600"]
