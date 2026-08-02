import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/core/di/injection.dart';
import 'package:backtrace/services/admin_service.dart';

final frontendAdminServiceProvider = Provider<FrontendAdminService>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return FrontendAdminService(apiClient);
});

class AdminDashboardState {
  final bool isLoading;
  final Map<String, dynamic>? metrics;
  final List<dynamic> users;
  final List<dynamic> auditLogs;
  final List<dynamic> pendingApprovals;
  final String? errorMessage;

  const AdminDashboardState({
    required this.isLoading,
    this.metrics,
    this.users = const [],
    this.auditLogs = const [],
    this.pendingApprovals = const [],
    this.errorMessage,
  });

  AdminDashboardState copyWith({
    bool? isLoading,
    Map<String, dynamic>? metrics,
    List<dynamic>? users,
    List<dynamic>? auditLogs,
    List<dynamic>? pendingApprovals,
    String? errorMessage,
  }) {
    return AdminDashboardState(
      isLoading: isLoading ?? this.isLoading,
      metrics: metrics ?? this.metrics,
      users: users ?? this.users,
      auditLogs: auditLogs ?? this.auditLogs,
      pendingApprovals: pendingApprovals ?? this.pendingApprovals,
      errorMessage: errorMessage,
    );
  }
}

class AdminDashboardNotifier extends StateNotifier<AdminDashboardState> {
  final FrontendAdminService _service;

  AdminDashboardNotifier(this._service) : super(const AdminDashboardState(isLoading: false)) {
    loadAdminDashboard();
  }

  Future<void> loadAdminDashboard() async {
    state = state.copyWith(isLoading: true);
    try {
      final dashRes = await _service.getDashboard();
      final userRes = await _service.getUsers();
      final auditRes = await _service.getAuditLogs();
      final appRes = await _service.getApprovals();

      state = state.copyWith(
        isLoading: false,
        metrics: dashRes['data'] as Map<String, dynamic>?,
        users: (userRes['data'] as List?) ?? [],
        auditLogs: (auditRes['data'] as List?) ?? [],
        pendingApprovals: (appRes['data'] as List?) ?? [],
      );
    } catch (e) {
      state = state.copyWith(isLoading: false, errorMessage: e.toString());
    }
  }
}

final adminDashboardProvider = StateNotifierProvider<AdminDashboardNotifier, AdminDashboardState>((ref) {
  final service = ref.watch(frontendAdminServiceProvider);
  return AdminDashboardNotifier(service);
});
