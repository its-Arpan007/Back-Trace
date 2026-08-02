import 'package:dio/dio.dart';
import 'package:backtrace/core/errors/app_exception.dart';

class ErrorInterceptor extends Interceptor {
  @override
  void onError(DioException err, ErrorInterceptorHandler handler) {
    AppException appException;

    switch (err.type) {
      case DioExceptionType.connectionTimeout:
      case DioExceptionType.sendTimeout:
      case DioExceptionType.receiveTimeout:
      case DioExceptionType.connectionError:
        appException = const NetworkException('Connection timeout or server unreachable');
        break;

      case DioExceptionType.badResponse:
        final statusCode = err.response?.statusCode;
        final responseData = err.response?.data;
        String errorMessage = 'An error occurred';
        String errorCode = 'SERVER_ERROR';

        if (responseData is Map<String, dynamic> && responseData.containsKey('error')) {
          final errorObj = responseData['error'];
          if (errorObj is Map<String, dynamic>) {
            errorMessage = errorObj['message'] ?? errorMessage;
            errorCode = errorObj['code'] ?? errorCode;
          }
        }

        if (statusCode == 401) {
          appException = UnauthorizedException(errorMessage);
        } else if (statusCode == 403) {
          appException = ForbiddenException(errorMessage);
        } else if (statusCode == 422) {
          appException = ValidationException(errorMessage);
        } else {
          appException = ServerException(
            errorMessage,
            code: errorCode,
            statusCode: statusCode,
          );
        }
        break;

      case DioExceptionType.cancel:
        appException = const UnknownException('Request cancelled');
        break;

      default:
        appException = UnknownException(err.message ?? 'An unexpected network error occurred');
        break;
    }

    final modifiedErr = DioException(
      requestOptions: err.requestOptions,
      error: appException,
      response: err.response,
      type: err.type,
    );

    handler.next(modifiedErr);
  }
}
