import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/widgets/status_badge.dart';
import 'package:backtrace/features/teacher_dashboard/presentation/controllers/teacher_dashboard_controller.dart';

class TeacherDashboardScreen extends ConsumerWidget {
  const TeacherDashboardScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(teacherDashboardProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Teacher Intelligence Hub'),
        actions: [
          IconButton(
            icon: const Icon(Icons.warning_amber_rounded, color: AppColors.error),
            onPressed: () => context.push('/intervention-center'),
          ),
          IconButton(
            icon: const Icon(Icons.build_rounded, color: AppColors.accentTeal),
            onPressed: () => context.push('/assessment-builder'),
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
                      StatusBadge(label: 'AUTOMATIC MONITORING LIVE', isOnline: true),
                      const Text('2 High-Risk Students', style: TextStyle(color: AppColors.error, fontWeight: FontWeight.bold, fontSize: 13)),
                    ],
                  ),
                  const SizedBox(height: 16),
                  Text('Classroom Intelligence Overview', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
                  const SizedBox(height: 8),
                  const Text('AI-powered classroom analytics aggregate misconceptions, decay curves, and prerequisite gaps across all assigned classes.', style: TextStyle(color: AppColors.textSecondaryDark)),
                  const SizedBox(height: 24),

                  // High-Risk Attention Banner
                  AppCard(
                    onTap: () => context.push('/intervention-center'),
                    child: Row(
                      children: [
                        Container(
                          width: 44,
                          height: 44,
                          decoration: BoxDecoration(color: AppColors.error.withOpacity(0.2), borderRadius: BorderRadius.circular(10)),
                          child: const Icon(Icons.error_outline_rounded, color: AppColors.error),
                        ),
                        const SizedBox(width: 14),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: const [
                              Text('STUDENT INTERVENTION NEEDED', style: TextStyle(color: AppColors.error, fontWeight: FontWeight.bold, fontSize: 11)),
                              SizedBox(height: 2),
                              Text('Jordan Lee (Sec A) • Persistent Stride Misconception', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 13)),
                            ],
                          ),
                        ),
                        const Icon(Icons.arrow_forward_ios_rounded, color: AppColors.textSecondaryDark, size: 14),
                      ],
                    ),
                  ),
                  const SizedBox(height: 24),

                  // Classes Section
                  Text('Assigned Classes', style: Theme.of(context).textTheme.titleLarge?.copyWith(color: Colors.white, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 12),
                  ...state.classes.map((c) {
                    return Padding(
                      padding: const EdgeInsets.only(bottom: 12.0),
                      child: AppCard(
                        onTap: () => context.push('/class-management'),
                        child: ListTile(
                          title: Text(c['class_name'] ?? 'Class', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                          subtitle: Text('Students: ${c['total_students']} • Avg Mastery: ${(c['average_mastery'] * 100).toStringAsFixed(0)}% • Weakness: ${c['weak_concept_code']}', style: const TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
                          trailing: const Icon(Icons.chevron_right_rounded, color: AppColors.textSecondaryDark),
                        ),
                      ),
                    );
                  }).toList(),
                  const SizedBox(height: 24),

                  // Navigation Grid
                  GridView.count(
                    crossAxisCount: 2,
                    shrinkWrap: true,
                    physics: const NeverScrollableScrollPhysics(),
                    crossAxisSpacing: 12,
                    mainAxisSpacing: 12,
                    childAspectRatio: 1.5,
                    children: [
                      _buildTile(context, 'Class Roster & Heatmaps', Icons.grid_on_rounded, AppColors.accentTeal, '/class-management'),
                      _buildTile(context, 'Assessment Builder', Icons.build_rounded, AppColors.accentCyan, '/assessment-builder'),
                      _buildTile(context, 'Assignments', Icons.assignment_rounded, AppColors.accentOrange, '/assignment-management'),
                      _buildTile(context, 'Class Reports & Exports', Icons.picture_as_pdf_rounded, AppColors.accentIndigo, '/teacher-reports'),
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
          Icon(icon, color: color, size: 28),
          const SizedBox(height: 8),
          Text(title, textAlign: TextAlign.center, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 12)),
        ],
      ),
    );
  }
}
