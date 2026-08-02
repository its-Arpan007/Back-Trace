import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/widgets/status_badge.dart';
import 'package:backtrace/features/student_dashboard/presentation/controllers/student_dashboard_controller.dart';

class StudentHomeDashboardScreen extends ConsumerWidget {
  const StudentHomeDashboardScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(studentDashboardProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('BACKTRACE Student Experience'),
        actions: [
          IconButton(
            icon: const Icon(Icons.notifications_none_rounded),
            onPressed: () => context.push('/notifications'),
          ),
          IconButton(
            icon: const Icon(Icons.person_outline_rounded),
            onPressed: () => context.push('/student-profile'),
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
                  // Welcome Header Card
                  AppCard(
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text('Welcome back, ${state.studentName}! 👋', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 18)),
                            const SizedBox(height: 4),
                            Text('${state.streakDays} Day Learning Streak 🔥', style: const TextStyle(color: AppColors.accentOrange, fontWeight: FontWeight.bold, fontSize: 13)),
                          ],
                        ),
                        StatusBadge(label: 'COGNITIVE TWIN LIVE', isOnline: true),
                      ],
                    ),
                  ),
                  const SizedBox(height: 16),

                  // Today's Plan Quick Launcher Card
                  AppCard(
                    onTap: () => context.push('/todays-learning-plan'),
                    child: Row(
                      children: [
                        Container(
                          width: 48,
                          height: 48,
                          decoration: BoxDecoration(color: AppColors.accentTeal.withOpacity(0.2), borderRadius: BorderRadius.circular(12)),
                          child: const Icon(Icons.today_rounded, color: AppColors.accentTeal),
                        ),
                        const SizedBox(width: 16),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: const [
                              Text("TODAY'S ADAPTIVE LEARNING PLAN", style: TextStyle(color: AppColors.accentTeal, fontWeight: FontWeight.bold, fontSize: 11)),
                              SizedBox(height: 2),
                              Text('3 Tasks • 45 Mins • Array Offset Focus', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 14)),
                            ],
                          ),
                        ),
                        const Icon(Icons.arrow_forward_ios_rounded, color: AppColors.textSecondaryDark, size: 16),
                      ],
                    ),
                  ),
                  const SizedBox(height: 24),

                  // Quick Action Buttons
                  Row(
                    children: [
                      Expanded(
                        child: ElevatedButton.icon(
                          onPressed: () => context.push('/session-launcher'),
                          icon: const Icon(Icons.play_circle_fill_rounded, size: 18),
                          label: const Text('Start Practice'),
                          style: ElevatedButton.styleFrom(backgroundColor: AppColors.accentTeal, minimumSize: const Size(0, 48)),
                        ),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: OutlinedButton.icon(
                          onPressed: () => context.push('/interactive-knowledge-map'),
                          icon: const Icon(Icons.account_tree_rounded, size: 18),
                          label: const Text('Knowledge Map'),
                          style: OutlinedButton.styleFrom(minimumSize: const Size(0, 48)),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 24),

                  // Motivational Insight & Weak Concepts
                  AppCard(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text('MOTIVATIONAL COGNITIVE INSIGHT', style: TextStyle(color: AppColors.accentCyan, fontWeight: FontWeight.bold, fontSize: 11, letterSpacing: 1.1)),
                        const SizedBox(height: 8),
                        Text(state.motivationalInsight, style: const TextStyle(color: Colors.white, fontSize: 14, fontWeight: FontWeight.w500)),
                        const Divider(color: AppColors.darkBorder),
                        const Text('Target Weak Concept: DSA_ARRAYS_01', style: TextStyle(color: AppColors.warning, fontWeight: FontWeight.bold, fontSize: 12)),
                      ],
                    ),
                  ),
                  const SizedBox(height: 24),

                  // Additional Feature Grid
                  GridView.count(
                    crossAxisCount: 2,
                    shrinkWrap: true,
                    physics: const NeverScrollableScrollPhysics(),
                    crossAxisSpacing: 12,
                    mainAxisSpacing: 12,
                    childAspectRatio: 1.5,
                    children: [
                      _buildGridTile(context, 'Progress & Velocity', Icons.speed_rounded, AppColors.accentTeal, '/student-progress-dashboard'),
                      _buildGridTile(context, 'Learning Goals', Icons.flag_rounded, AppColors.accentCyan, '/student-goals'),
                      _buildGridTile(context, 'Recommendations', Icons.auto_awesome_rounded, AppColors.accentOrange, '/recommendation-dashboard'),
                      _buildGridTile(context, 'Settings & Sync', Icons.settings_rounded, AppColors.accentIndigo, '/app-settings'),
                    ],
                  ),
                ],
              ),
            ),
    );
  }

  Widget _buildGridTile(BuildContext context, String title, IconData icon, Color color, String route) {
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
