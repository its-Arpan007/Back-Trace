import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/features/progress/presentation/controllers/progress_controller.dart';

class StudentProgressDashboardScreen extends ConsumerWidget {
  const StudentProgressDashboardScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(progressProvider);

    return Scaffold(
      appBar: AppBar(title: const Text('Student Mastery & Velocity Progress')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('COGNITIVE MASTERY OVERVIEW', style: TextStyle(color: AppColors.accentTeal, fontWeight: FontWeight.bold, fontSize: 11)),
                const SizedBox(height: 8),
                Text('${(state.overallMastery * 100).toStringAsFixed(1)}%', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 32)),
                const SizedBox(height: 4),
                const Text('Learning Velocity: 1.45x concepts / week • Streak: 7 Days 🔥', style: TextStyle(color: AppColors.textSecondaryDark, fontSize: 13)),
              ],
            ),
          ),
          const SizedBox(height: 16),

          ElevatedButton.icon(
            onPressed: () => context.push('/concept-timeline'),
            icon: const Icon(Icons.timeline_rounded),
            label: const Text('View Concept Learning Progression Timeline'),
            style: ElevatedButton.styleFrom(backgroundColor: AppColors.accentTeal, minimumSize: const Size(double.infinity, 50)),
          ),
        ],
      ),
    );
  }
}
