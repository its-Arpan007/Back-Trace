import 'package:dio/dio.dart';

class RetryInterceptor extends Interceptor {
  final int maxRetries;
  final int retryIntervalMs;

  RetryInterceptor({this.maxRetries = 3, this.retryIntervalMs = 1000});

  @override
  void onError(DioException err, ErrorInterceptorHandler handler) async {
    final requestOptions = err.requestOptions;
    final retryCount = requestOptions.extra['retry_count'] ?? 0;

    if (_shouldRetry(err) && retryCount < maxRetries) {
      requestOptions.extra['retry_count'] = retryCount + 1;
      await Future.delayed(Duration(milliseconds: retryIntervalMs * (retryCount + 1)));

      try {
        final dio = Dio();
        final response = await dio.fetch(requestOptions);
        return handler.resolve(response);
      } catch (e) {
        return super.onError(err, handler);
      }
    }

    super.onError(err, handler);
  }

  bool _shouldRetry(DioException err) {
    return err.type == DioExceptionType.connectionTimeout ||
        err.type == DioExceptionType.receiveTimeout ||
        err.type == DioExceptionType.connectionError;
  }
}
