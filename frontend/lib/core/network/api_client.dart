import 'package:dio/dio.dart';
import 'package:backtrace/core/errors/app_exception.dart';
import 'package:backtrace/core/network/dio_client.dart';

class ApiClient {
  final DioClient _dioClient;

  ApiClient(this._dioClient);

  Future<dynamic> get(
    String path, {
    Map<String, dynamic>? queryParameters,
    Options? options,
  }) async {
    try {
      final response = await _dioClient.dio.get(
        path,
        queryParameters: queryParameters,
        options: options,
      );
      return response.data;
    } on DioException catch (e) {
      if (e.error is AppException) throw e.error as AppException;
      throw UnknownException(e.message ?? 'HTTP GET request failed');
    }
  }

  Future<dynamic> post(
    String path, {
    dynamic data,
    Map<String, dynamic>? queryParameters,
    Options? options,
  }) async {
    try {
      final response = await _dioClient.dio.post(
        path,
        data: data,
        queryParameters: queryParameters,
        options: options,
      );
      return response.data;
    } on DioException catch (e) {
      if (e.error is AppException) throw e.error as AppException;
      throw UnknownException(e.message ?? 'HTTP POST request failed');
    }
  }

  Future<dynamic> put(
    String path, {
    dynamic data,
    Map<String, dynamic>? queryParameters,
    Options? options,
  }) async {
    try {
      final response = await _dioClient.dio.put(
        path,
        data: data,
        queryParameters: queryParameters,
        options: options,
      );
      return response.data;
    } on DioException catch (e) {
      if (e.error is AppException) throw e.error as AppException;
      throw UnknownException(e.message ?? 'HTTP PUT request failed');
    }
  }

  Future<dynamic> delete(
    String path, {
    dynamic data,
    Map<String, dynamic>? queryParameters,
    Options? options,
  }) async {
    try {
      final response = await _dioClient.dio.delete(
        path,
        data: data,
        queryParameters: queryParameters,
        options: options,
      );
      return response.data;
    } on DioException catch (e) {
      if (e.error is AppException) throw e.error as AppException;
      throw UnknownException(e.message ?? 'HTTP DELETE request failed');
    }
  }
}
