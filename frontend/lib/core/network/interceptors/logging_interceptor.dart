import 'package:dio/dio.dart';
import 'package:backtrace/utils/logger.dart';

class LoggingInterceptor extends Interceptor {
  @override
  void onRequest(RequestOptions options, RequestInterceptorHandler handler) {
    AppLogger.d('--> ${options.method.toUpperCase()} ${options.uri}');
    AppLogger.d('Headers: ${options.headers}');
    if (options.data != null) {
      AppLogger.d('Body: ${options.data}');
    }
    super.onRequest(options, handler);
  }

  @override
  void onResponse(Response response, ResponseInterceptorHandler handler) {
    AppLogger.d('<-- ${response.statusCode} ${response.requestOptions.uri}');
    AppLogger.d('Response Data: ${response.data}');
    super.onResponse(response, handler);
  }

  @override
  void onError(DioException err, ErrorInterceptorHandler handler) {
    AppLogger.e('<-- ERROR ${err.response?.statusCode} ${err.requestOptions.uri}');
    AppLogger.e('Error Message: ${err.message}');
    super.onError(err, handler);
  }
}
