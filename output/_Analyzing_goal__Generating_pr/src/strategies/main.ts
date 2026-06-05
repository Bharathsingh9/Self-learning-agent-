// Project root entry point
import { Config, EnvironmentVariables } from './config/config';
import { GroqClient } from '@groq/sanity-client';

// Initialize the client with config and environment variables
const client = new GroqClient(config.models, process.env)

// Initialize the system based on the client and config
init(client, config)