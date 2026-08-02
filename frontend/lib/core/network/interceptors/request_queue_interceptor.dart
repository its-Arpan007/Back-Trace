import 'package:dio/dio.dart';

class RequestQueueInterceptor extends Interceptor {
  final List<RequestOptions> _requestQueue = [];
  bool isOffline = false;

  @override
  void onRequest(RequestOptions options, RequestInterceptorHandler handler) {
    if (isOffline) {
      _requestQueue.add(options);
    }
    super.onRequest(options, handler);
  }

  void processQueue(Dio dio) async {
    while (_requestQueue.isNotEmpty) {
      final req = _requestQueue.removeAt(0);
      try {
        await dio.fetch(req);
      } catch (_) {}
    }
  }
}
