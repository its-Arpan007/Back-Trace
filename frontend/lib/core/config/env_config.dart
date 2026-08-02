enum Environment { dev, staging, prod }

class EnvConfig {
  static const Environment environment = Environment.dev;
  static const String appName = 'BACKTRACE';
  static const String appTagline = 'AI-Powered Learning Intelligence Platform';
  
  static String get baseUrl {
    switch (environment) {
      case Environment.dev:
        return 'http://localhost:8000/api/v1';
      case Environment.staging:
        return 'https://staging-api.backtrace.ai/api/v1';
      case Environment.prod:
        return 'https://api.backtrace.ai/api/v1';
    }
  }

  static const int connectTimeoutMs = 10000;
  static const int receiveTimeoutMs = 10000;
  static const bool enableNetworkLogs = true;
}
