import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AdaptiveLearningPathScreen extends StatelessWidget {
  const AdaptiveLearningPathScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final nodes = [
      {"step": "Step 1", "name": "Comparison Operators", "status": "Mastered (100%)", "color": AppColors.success},
      {"step": "Step 2", "name": "Array Memory Layout", "status": "In Remediation (65%)", "color": AppColors.warning},
      {"step": "Step 3", "name": "Sorted Arrays", "status": "Locked (Prereq Gap)", "color": AppColors.textSecondaryDark},
      {"step": "Step 4", "name": "Binary Search", "status": "Target Mastery Goal", "color": AppColors.accentTeal},
    ];

    return Scaffold(
      appBar: AppBar(title: const Text('Dynamic Adaptive Learning Path')),
      body: ListView.builder(
        padding: const EdgeInsets.all(24),
        itemCount: nodes.length,
        itemBuilder: (context, idx) {
          final n = nodes[idx];
          return Column(
            children: [
              AppCard(
                child: ListTile(
                  leading: CircleAvatar(
                    backgroundColor: n["color"] as Color,
                    child: Text('${idx + 1}', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                  ),
                  title: Text('${n["name"]}', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                  subtitle: Text(n["status"] as String, style: TextStyle(color: n["color"] as Color, fontSize: 12)),
                ),
              ),
              if (idx < nodes.length - 1)
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
