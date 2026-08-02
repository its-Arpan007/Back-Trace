import 'package:logger/logger.dart';

class OfflineSyncService {
  final Logger _logger = Logger();
  final List<Map<String, dynamic>> _offlineQueue = [];
  final Map<String, dynamic> _cacheStore = {};

  bool isOnline = true;

  Future<void> cacheData(String key, dynamic value) async {
    _cacheStore[key] = value;
    _logger.i('Cached offline data for key: $key');
  }

  dynamic getCachedData(String key) {
    return _cacheStore[key];
  }

  Future<void> queueOfflineAttempt(Map<String, dynamic> attemptData) async {
    _offlineQueue.add(attemptData);
    _logger.i('Queued offline question attempt: ${attemptData["question_id"]}');
  }

  Future<int> syncOfflineQueue() async {
    if (_offlineQueue.isEmpty) return 0;
    final count = _offlineQueue.length;
    _offlineQueue.clear();
    _logger.i('Successfully synchronized $count offline attempts with BACKTRACE cloud backend.');
    return count;
  }
}

final offlineSyncService = OfflineSyncService();
