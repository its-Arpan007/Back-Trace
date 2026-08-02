import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/core/di/injection.dart';
import 'package:backtrace/services/analytics_service.dart';

final frontendAnalyticsServiceProvider = Provider<FrontendAnalyticsService>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return FrontendAnalyticsService(apiClient);
});

class AnalyticsState {
  final bool isLoading;
  final Map<String, dynamic>? studentMetrics;
  final Map<String, dynamic>? predictions;
  final Map<String, dynamic>? reports;
  final String? errorMessage;

  const AnalyticsState({
    required this.isLoading,
    this.studentMetrics,
    this.predictions,
    this.reports,
    this.errorMessage,
  });

  AnalyticsState copyWith({
    bool? isLoading,
    Map<String, dynamic>? studentMetrics,
    Map<String, dynamic>? predictions,
    Map<String, dynamic>? reports,
    String? errorMessage,
  }) {
    return AnalyticsState(
      isLoading: isLoading ?? this.isLoading,
      studentMetrics: studentMetrics ?? this.studentMetrics,
      predictions: predictions ?? this.predictions,
      reports: reports ?? this.reports,
      errorMessage: errorMessage,
    );
  }
}

class AnalyticsNotifier extends StateNotifier<AnalyticsState> {
  final FrontendAnalyticsService _service;

  AnalyticsNotifier(this._service) : super(const AnalyticsState(isLoading: false)) {
    loadAnalytics("11111111-1111-1111-1111-111111111111");
  }

  Future<void> loadAnalytics(String studentId) async {
    state = state.copyWith(isLoading: true);
    try {
      final res = await _service.getStudentAnalytics(studentId);
      final predRes = await _service.getPredictions(studentId);
      final repRes = await _service.getReports(studentId);

      if (res['success'] == true && res['data'] != null) {
        state = state.copyWith(
          isLoading: false,
          studentMetrics: res['data'] as Map<String, dynamic>,
          predictions: predRes['data'] as Map<String, dynamic>?,
          reports: repRes['data'] as Map<String, dynamic>?,
        );
      } else {
        state = state.copyWith(isLoading: false, errorMessage: res['message']);
      }
    } catch (e) {
      state = state.copyWith(isLoading: false, errorMessage: e.toString());
    }
  }
}

final analyticsProvider = StateNotifierProvider<AnalyticsNotifier, AnalyticsState>((ref) {
  final service = ref.watch(frontendAnalyticsServiceProvider);
  return AnalyticsNotifier(service);
});
