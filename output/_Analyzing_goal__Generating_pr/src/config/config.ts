# Configuration options
import { EnvironmentVariables } from './types/env';
import { defaultModels } from './models/models';

export interface Config {
  models: typeof defaultModels;
}

export const config: Config = {
  ...defaultModels,
  // Other configurations as needed
};