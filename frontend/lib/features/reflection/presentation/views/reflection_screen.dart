import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/features/reflection/presentation/controllers/reflection_controller.dart';

class ReflectionScreen extends ConsumerWidget {
  const ReflectionScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(reflectionProvider);
    final notifier = ref.read(reflectionProvider.notifier);

    return Scaffold(
      appBar: AppBar(title: const Text('Cognitive Self-Reflection Prompt')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        children: [
          Text('Reflect on Your Problem-Solving Logic', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
          const SizedBox(height: 8),
          const Text('Self-reflection refines your cognitive model and provides calibration feedback to the Student Learning Model.', style: TextStyle(color: AppColors.textSecondaryDark)),
          const SizedBox(height: 24),

          // Question 1: Why did you choose this answer?
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('1. Why did you choose this answer?', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                const SizedBox(height: 8),
                TextField(
                  onChanged: notifier.setWhyChoice,
                  decoration: const InputDecoration(
                    hintText: 'e.g. Added base address directly to index 5...',
                    border: OutlineInputBorder(),
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 16),

          // Question 2: What confused you during calculation?
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('2. What confused you during this problem?', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                const SizedBox(height: 8),
                TextField(
                  onChanged: notifier.setConfusionLog,
                  decoration: const InputDecoration(
                    hintText: 'e.g. Forgot that 4-byte stride multiplier is required...',
                    border: OutlineInputBorder(),
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 24),

          ElevatedButton.icon(
            onPressed: () {
              notifier.submitReflection();
              context.push('/diagnosis-report');
            },
            icon: const Icon(Icons.check_rounded),
            label: const Text('Submit Reflection & View Diagnosis'),
            style: ElevatedButton.styleFrom(backgroundColor: AppColors.accentTeal, minimumSize: const Size(double.infinity, 50)),
          ),
        ],
      ),
    );
  }
}
