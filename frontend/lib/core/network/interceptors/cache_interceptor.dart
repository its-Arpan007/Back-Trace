import 'package:dio/dio.dart';

class CacheInterceptor extends Interceptor {
  final Map<String, Response> _cache = {};

  @override
  void onRequest(RequestOptions options, RequestInterceptorHandler handler) {
    if (options.method == 'GET') {
      final cacheKey = options.uri.toString();
      if (_cache.containsKey(cacheKey)) {
        final cachedResponse = _cache[cacheKey]!;
        return handler.resolve(cachedResponse);
      }
    }
    super.onRequest(options, handler);
  }

  @override
  void onResponse(Response response, ResponseInterceptorHandler handler) {
    if (response.requestOptions.method == 'GET' && response.statusCode == 200) {
      _cache[response.requestOptions.uri.toString()] = response;
    }
    super.onResponse(response, handler);
  }
}
