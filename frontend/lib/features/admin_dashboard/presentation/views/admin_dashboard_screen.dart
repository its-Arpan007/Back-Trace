import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/widgets/status_badge.dart';
import 'package:backtrace/features/admin_dashboard/presentation/controllers/admin_dashboard_controller.dart';

class AdminDashboardScreen extends ConsumerWidget {
  const AdminDashboardScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(adminDashboardProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Enterprise Admin & Content Platform'),
        actions: [
          IconButton(
            icon: const Icon(Icons.monitor_heart_rounded, color: AppColors.accentTeal),
            onPressed: () => context.push('/admin-system-monitoring'),
          ),
          IconButton(
            icon: const Icon(Icons.security_rounded, color: AppColors.accentCyan),
            onPressed: () => context.push('/admin-audit-center'),
          ),
        ],
      ),
      body: state.isLoading
          ? const Center(child: CircularProgressIndicator(color: AppColors.accentTeal))
          : SingleChildScrollView(
              padding: const EdgeInsets.all(24),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      StatusBadge(label: 'SYSTEM HEALTH: HEALTHY (99.9%)', isOnline: true),
                      const Text('Storage: 12.4 GB', style: TextStyle(color: AppColors.accentTeal, fontWeight: FontWeight.bold, fontSize: 13)),
                    ],
                  ),
                  const SizedBox(height: 16),
                  Text('Enterprise Governance & Operations', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
                  const SizedBox(height: 8),
                  const Text('Comprehensive administration of platform users, curriculum, knowledge graph editor, AI prompts, system health, and audit logs.', style: TextStyle(color: AppColors.textSecondaryDark)),
                  const SizedBox(height: 24),

                  // System Status Grid
                  Row(
                    children: [
                      Expanded(
                        child: AppCard(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: const [
                              Text('Active Users', style: TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
                              SizedBox(height: 4),
                              Text('150', style: TextStyle(color: AppColors.accentTeal, fontWeight: FontWeight.bold, fontSize: 22)),
                              SizedBox(height: 4),
                              Text('Students & Teachers', style: TextStyle(color: AppColors.success, fontSize: 11)),
                            ],
                          ),
                        ),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: AppCard(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: const [
                              Text('Pending Approvals', style: TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
                              SizedBox(height: 4),
                              Text('3 Items', style: TextStyle(color: AppColors.accentOrange, fontWeight: FontWeight.bold, fontSize: 22)),
                              SizedBox(height: 4),
                              Text('Questions & Graph Nodes', style: TextStyle(color: AppColors.warning, fontSize: 11)),
                            ],
                          ),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 24),

                  // Admin Navigation Grid
                  GridView.count(
                    crossAxisCount: 2,
                    shrinkWrap: true,
                    physics: const NeverScrollableScrollPhysics(),
                    crossAxisSpacing: 12,
                    mainAxisSpacing: 12,
                    childAspectRatio: 1.4,
                    children: [
                      _buildTile(context, 'User & RBAC Matrix', Icons.people_alt_rounded, AppColors.accentTeal, '/admin-user-management'),
                      _buildTile(context, 'Curriculum CMS', Icons.menu_book_rounded, AppColors.accentCyan, '/admin-curriculum-management'),
                      _buildTile(context, 'Knowledge Graph Editor', Icons.account_tree_rounded, AppColors.accentOrange, '/admin-knowledge-graph-editor'),
                      _buildTile(context, 'Question Bank CMS', Icons.quiz_rounded, AppColors.accentIndigo, '/admin-question-bank'),
                      _buildTile(context, 'Educational Resources', Icons.video_library_rounded, AppColors.success, '/admin-resource-management'),
                      _buildTile(context, 'AI Prompts & Flags', Icons.psychology_rounded, AppColors.warning, '/admin-ai-config'),
                      _buildTile(context, 'System Health & Metrics', Icons.monitor_heart_rounded, AppColors.accentTeal, '/admin-system-monitoring'),
                      _buildTile(context, 'Approval Queue', Icons.fact_check_rounded, AppColors.accentCyan, '/admin-approval-center'),
                      _buildTile(context, 'Audit Log Center', Icons.history_rounded, AppColors.accentOrange, '/admin-audit-center'),
                      _buildTile(context, 'Backup & Restore', Icons.cloud_download_rounded, AppColors.accentIndigo, '/admin-backup-restore'),
                    ],
                  ),
                ],
              ),
            ),
    );
  }

  Widget _buildTile(BuildContext context, String title, IconData icon, Color color, String route) {
    return AppCard(
      onTap: () => context.push(route),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(icon, color: color, size: 26),
          const SizedBox(height: 6),
          Text(title, textAlign: TextAlign.center, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 11)),
        ],
      ),
    );
  }
}
