import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/features/learning_session/presentation/controllers/learning_session_controller.dart';

class SessionLauncherScreen extends ConsumerWidget {
  const SessionLauncherScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(learningSessionProvider);
    final notifier = ref.read(learningSessionProvider.notifier);

    final modes = [
      {'key': 'adaptive', 'name': 'Adaptive Practice', 'desc': 'Generates questions targeting your specific prerequisite gaps.'},
      {'key': 'revision', 'name': 'Spaced Revision Session', 'desc': 'Reviews concepts flagged by Ebbinghaus decay curve.'},
      {'key': 'challenge', 'name': 'High-Mastery Challenge', 'desc': 'Tests complex multi-dimensional Bloom level problems.'},
      {'key': 'exam', 'name': 'Timed Exam Mode', 'desc': 'Simulates strict time-constrained diagnostic assessment.'},
      {'key': 'quick', 'name': 'Quick 3-Question Practice', 'desc': 'Fast 5-minute session for quick daily retention.'},
    ];

    return Scaffold(
      appBar: AppBar(title: const Text('Configure Practice Session')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          Text('Select Learning Session Mode', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
          const SizedBox(height: 8),
          const Text('Every question attempt updates your Bayesian Knowledge State and triggers instant root-cause diagnosis.', style: TextStyle(color: AppColors.textSecondaryDark)),
          const SizedBox(height: 24),

          ...modes.map((m) {
            final isSel = state.sessionMode == m['key'];
            return Padding(
              padding: const EdgeInsets.only(bottom: 12.0),
              child: AppCard(
                onTap: () => notifier.setSessionMode(m['key']!),
                child: Row(
                  children: [
                    Radio<String>(
                      value: m['key']!,
                      groupValue: state.sessionMode,
                      onChanged: (val) => notifier.setSessionMode(val!),
                      activeColor: AppColors.accentTeal,
                    ),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(m['name']!, style: TextStyle(color: isSel ? AppColors.accentTeal : Colors.white, fontWeight: FontWeight.bold, fontSize: 15)),
                          const SizedBox(height: 2),
                          Text(m['desc']!, style: const TextStyle(color: AppColors.textSecondaryDark, fontSize: 12)),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            );
          }).toList(),
          const SizedBox(height: 24),

          ElevatedButton.icon(
            onPressed: () => context.push('/question-player'),
            icon: const Icon(Icons.play_arrow_rounded, size: 22),
            label: const Text('Launch Practice Session'),
            style: ElevatedButton.styleFrom(backgroundColor: AppColors.accentTeal, minimumSize: const Size(double.infinity, 52)),
          ),
        ],
      ),
    );
  }
}
