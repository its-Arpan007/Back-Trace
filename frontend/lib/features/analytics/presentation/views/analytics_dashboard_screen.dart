import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/widgets/status_badge.dart';
import 'package:backtrace/features/analytics/presentation/controllers/analytics_controller.dart';

class AnalyticsDashboardScreen extends ConsumerWidget {
  const AnalyticsDashboardScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(analyticsProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Learning Analytics Platform'),
        actions: [
          IconButton(
            icon: const Icon(Icons.analytics_rounded, color: AppColors.accentTeal),
            onPressed: () => context.push('/prediction-dashboard'),
          ),
          IconButton(
            icon: const Icon(Icons.picture_as_pdf_rounded, color: AppColors.accentCyan),
            onPressed: () => context.push('/performance-reports'),
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
                      StatusBadge(label: 'ANALYTICS PIPELINE ACTIVE', isOnline: true),
                      const Text('Velocity: 1.45x', style: TextStyle(color: AppColors.accentTeal, fontWeight: FontWeight.bold, fontSize: 13)),
                    ],
                  ),
                  const SizedBox(height: 16),
                  Text('Cognitive Learning Progress', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
                  const SizedBox(height: 8),
                  const Text('Multi-dimensional analytics aggregating diagnostic events, BKT mastery, and retention trends.', style: TextStyle(color: AppColors.textSecondaryDark)),
                  const SizedBox(height: 24),

                  // Analytics Cards Grid
                  Row(
                    children: [
                      Expanded(
                        child: AppCard(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: const [
                              Text('Progress', style: TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
                              SizedBox(height: 4),
                              Text('78.5%', style: TextStyle(color: AppColors.accentTeal, fontWeight: FontWeight.bold, fontSize: 22)),
                              SizedBox(height: 4),
                              Text('+18% last 14d', style: TextStyle(color: AppColors.success, fontSize: 11)),
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
                              Text('Readiness', style: TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
                              SizedBox(height: 4),
                              Text('82.0%', style: TextStyle(color: AppColors.accentCyan, fontWeight: FontWeight.bold, fontSize: 22)),
                              SizedBox(height: 4),
                              Text('Low Failure Risk', style: TextStyle(color: AppColors.success, fontSize: 11)),
                            ],
                          ),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 24),

                  // Explainable Natural Language Insight Card
                  AppCard(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: const [
                        Text('EXPLAINABLE COGNITIVE INSIGHT', style: TextStyle(color: AppColors.accentTeal, fontWeight: FontWeight.bold, fontSize: 11, letterSpacing: 1.1)),
                        SizedBox(height: 8),
                        Text('Student mastery has increased by 18% over the last 14 days.', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 15)),
                        SizedBox(height: 6),
                        Text('Why: Completed 3 practice sessions and resolved array stride offset misconception via interactive visualizers.', style: TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
                      ],
                    ),
                  ),
                  const SizedBox(height: 24),

                  // Navigation Actions
                  Row(
                    children: [
                      Expanded(
                        child: OutlinedButton.icon(
                          onPressed: () => context.push('/learning-heatmap'),
                          icon: const Icon(Icons.grid_on_rounded, size: 16),
                          label: const Text('Heatmap'),
                        ),
                      ),
                      const SizedBox(width: 8),
                      Expanded(
                        child: OutlinedButton.icon(
                          onPressed: () => context.push('/teacher-insights'),
                          icon: const Icon(Icons.insights_rounded, size: 16),
                          label: const Text('Teacher'),
                        ),
                      ),
                      const SizedBox(width: 8),
                      Expanded(
                        child: OutlinedButton.icon(
                          onPressed: () => context.push('/institution-dashboard'),
                          icon: const Icon(Icons.account_balance_rounded, size: 16),
                          label: const Text('Admin'),
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
