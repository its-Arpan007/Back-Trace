import 'package:dio/dio.dart';
import 'package:backtrace/core/config/env_config.dart';
import 'package:backtrace/core/network/interceptors/auth_interceptor.dart';
import 'package:backtrace/core/network/interceptors/cache_interceptor.dart';
import 'package:backtrace/core/network/interceptors/error_interceptor.dart';
import 'package:backtrace/core/network/interceptors/logging_interceptor.dart';
import 'package:backtrace/core/network/interceptors/request_queue_interceptor.dart';
import 'package:backtrace/core/network/interceptors/retry_interceptor.dart';

class DioClient {
  late final Dio dio;
  final AuthInterceptor authInterceptor = AuthInterceptor();
  final RetryInterceptor retryInterceptor = RetryInterceptor();
  final CacheInterceptor cacheInterceptor = CacheInterceptor();
  final RequestQueueInterceptor requestQueueInterceptor = RequestQueueInterceptor();

  DioClient() {
    dio = Dio(
      BaseOptions(
        baseUrl: EnvConfig.baseUrl,
        connectTimeout: const Duration(milliseconds: EnvConfig.connectTimeoutMs),
        receiveTimeout: const Duration(milliseconds: EnvConfig.receiveTimeoutMs),
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
      ),
    );

    dio.interceptors.addAll([
      authInterceptor,
      retryInterceptor,
      cacheInterceptor,
      requestQueueInterceptor,
      if (EnvConfig.enableNetworkLogs) LoggingInterceptor(),
      ErrorInterceptor(),
    ]);
  }
}
