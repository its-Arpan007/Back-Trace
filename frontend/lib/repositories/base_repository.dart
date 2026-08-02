import 'package:backtrace/core/errors/app_exception.dart';
import 'package:backtrace/core/errors/failure.dart';
import 'package:backtrace/shared/result.dart';

abstract class BaseRepository {
  Future<Result<T>> safeCall<T>(Future<T> Function() call) async {
    try {
      final data = await call();
      return Result.success(data);
    } on NetworkException catch (e) {
      return Result.failure(NetworkFailure(e.message));
    } on UnauthorizedException catch (e) {
      return Result.failure(AuthFailure(e.message));
    } on ServerException catch (e) {
      return Result.failure(ServerFailure(e.message, code: e.code));
    } on AppException catch (e) {
      return Result.failure(ServerFailure(e.message, code: e.code));
    } catch (e) {
      return Result.failure(ServerFailure('Unexpected error: ${e.toString()}'));
    }
  }
}
