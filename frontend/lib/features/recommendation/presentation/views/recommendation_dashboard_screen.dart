import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/widgets/status_badge.dart';
import 'package:backtrace/features/recommendation/presentation/controllers/recommendation_controller.dart';

class RecommendationDashboardScreen extends ConsumerWidget {
  const RecommendationDashboardScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(recommendationProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Adaptive Recommendation Hub'),
        actions: [
          IconButton(
            icon: const Icon(Icons.today_rounded, color: AppColors.accentTeal),
            onPressed: () => context.push('/todays-learning-plan'),
          ),
          IconButton(
            icon: const Icon(Icons.alt_route_rounded, color: AppColors.accentCyan),
            onPressed: () => context.push('/adaptive-learning-path'),
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
                      StatusBadge(label: 'COGNITIVE ADAPTIVITY ACTIVE', isOnline: true),
                      const Text('3 Recommended Actions', style: TextStyle(color: AppColors.accentCyan, fontWeight: FontWeight.bold, fontSize: 12)),
                    ],
                  ),
                  const SizedBox(height: 16),
                  Text('Personalized Remediation Actions', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
                  const SizedBox(height: 8),
                  const Text('Explainable learning steps derived from your latest diagnostic reports and BKT mastery state.', style: TextStyle(color: AppColors.textSecondaryDark)),
                  const SizedBox(height: 24),

                  // Priority Recommendation Card 1
                  AppCard(
                    onTap: () => context.push('/recommended-resources'),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: const [
                            Text('RESOURCE RECOMMENDATION • CRITICAL', style: TextStyle(color: AppColors.error, fontWeight: FontWeight.bold, fontSize: 11, letterSpacing: 1.1)),
                            Text('10 Mins', style: TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
                          ],
                        ),
                        const SizedBox(height: 8),
                        const Text('Interactive Visualizer: Array Memory Stride', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16)),
                        const SizedBox(height: 6),
                        const Text('Why: Recommended because your latest diagnosis revealed a Concept Gap in DSA_ARRAYS_01.', style: TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
                        const SizedBox(height: 12),
                        ElevatedButton.icon(
                          onPressed: () => context.push('/recommended-resources'),
                          icon: const Icon(Icons.play_arrow_rounded, size: 18),
                          label: const Text('Start Resource Session'),
                          style: ElevatedButton.styleFrom(backgroundColor: AppColors.accentTeal),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 16),

                  // Priority Recommendation Card 2
                  AppCard(
                    onTap: () => context.push('/recommended-questions'),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: const [
                            Text('PRACTICE RECOMMENDATION • HIGH', style: TextStyle(color: AppColors.warning, fontWeight: FontWeight.bold, fontSize: 11, letterSpacing: 1.1)),
                            Text('15 Mins', style: TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
                          ],
                        ),
                        const SizedBox(height: 8),
                        const Text('Targeted Practice: 2 Offset Math Questions', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16)),
                        const SizedBox(height: 6),
                        const Text('Why: Validates memory address calculation under target Bloom level: Apply.', style: TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
                      ],
                    ),
                  ),
                  const SizedBox(height: 24),

                  Row(
                    children: [
                      Expanded(
                        child: OutlinedButton.icon(
                          onPressed: () => context.push('/revision-queue'),
                          icon: const Icon(Icons.history_toggle_off_rounded, size: 16),
                          label: const Text('Revision Queue'),
                        ),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: OutlinedButton.icon(
                          onPressed: () => context.push('/goal-dashboard'),
                          icon: const Icon(Icons.flag_rounded, size: 16),
                          label: const Text('Learning Goals'),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
    );
  }
}
