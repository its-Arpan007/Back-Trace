import 'package:dio/dio.dart';
import 'package:backtrace/core/constants/api_constants.dart';

class AuthInterceptor extends Interceptor {
  String? _accessToken;

  void setToken(String? token) {
    _accessToken = token;
  }

  String? get currentToken => _accessToken;

  @override
  void onRequest(RequestOptions options, RequestInterceptorHandler handler) {
    if (_accessToken != null && _accessToken!.isNotEmpty) {
      options.headers[ApiConstants.authorizationHeader] =
          '${ApiConstants.bearerPrefix}$_accessToken';
    }
    super.onRequest(options, handler);
  }

  @override
  void onError(DioException err, ErrorInterceptorHandler handler) async {
    if (err.response?.statusCode == 401) {
      // 401 Unauthorized handling hook
    }
    super.onError(err, handler);
  }
}
