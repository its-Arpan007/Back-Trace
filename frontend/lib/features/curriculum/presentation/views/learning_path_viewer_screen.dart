import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class LearningPathViewerScreen extends StatelessWidget {
  const LearningPathViewerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final sequence = ['DSA_ARRAYS_01', 'DSA_TREES_01', 'DSA_GRAPH_01'];

    return Scaffold(
      appBar: AppBar(title: const Text('Optimal Remediation & Learning Path')),
      body: ListView.builder(
        padding: const EdgeInsets.all(24),
        itemCount: sequence.length,
        itemBuilder: (context, index) {
          final code = sequence[index];
          final isTarget = index == sequence.length - 1;
          return Column(
            children: [
              AppCard(
                child: ListTile(
                  leading: CircleAvatar(
                    backgroundColor: isTarget ? AppColors.accentCyan : AppColors.accentTeal,
                    child: Text('${index + 1}', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                  ),
                  title: Text(code, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                  subtitle: Text(isTarget ? 'Target Concept Goal' : 'Prerequisite Concept Dependency', style: const TextStyle(color: AppColors.textSecondaryDark)),
                ),
              ),
              if (index < sequence.length - 1)
                const Padding(
                  padding: EdgeInsets.symmetric(vertical: 8.0),
                  child: Icon(Icons.arrow_downward_rounded, color: AppColors.accentTeal),
                ),
            ],
          );
        },
      ),
    );
  }
}
