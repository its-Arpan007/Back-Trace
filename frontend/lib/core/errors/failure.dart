abstract class Failure {
  final String message;
  final String? code;

  const Failure(this.message, {this.code});

  @override
  String toString() => '$runtimeType: $message';
}

class ServerFailure extends Failure {
  const ServerFailure(String message, {String? code}) : super(message, code: code);
}

class NetworkFailure extends Failure {
  const NetworkFailure([String message = 'Network connection failed'])
      : super(message, code: 'NETWORK_FAILURE');
}

class AuthFailure extends Failure {
  const AuthFailure(String message) : super(message, code: 'AUTH_FAILURE');
}

class CacheFailure extends Failure {
  const CacheFailure(String message) : super(message, code: 'CACHE_FAILURE');
}
