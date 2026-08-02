abstract class AppException implements Exception {
  final String message;
  final String? code;
  final int? statusCode;

  const AppException(this.message, {this.code, this.statusCode});

  @override
  String toString() => 'AppException: $message (code: $code, statusCode: $statusCode)';
}

class NetworkException extends AppException {
  const NetworkException([String message = 'No internet connection or server unreachable'])
      : super(message, code: 'NETWORK_ERROR');
}

class ServerException extends AppException {
  const ServerException(String message, {String? code, int? statusCode})
      : super(message, code: code ?? 'SERVER_ERROR', statusCode: statusCode);
}

class UnauthorizedException extends AppException {
  const UnauthorizedException([String message = 'Unauthorized access'])
      : super(message, code: 'UNAUTHORIZED', statusCode: 401);
}

class ForbiddenException extends AppException {
  const ForbiddenException([String message = 'Forbidden operation'])
      : super(message, code: 'FORBIDDEN', statusCode: 403);
}

class ValidationException extends AppException {
  const ValidationException(String message)
      : super(message, code: 'VALIDATION_ERROR', statusCode: 422);
}

class UnknownException extends AppException {
  const UnknownException([String message = 'An unexpected error occurred'])
      : super(message, code: 'UNKNOWN_ERROR');
}
