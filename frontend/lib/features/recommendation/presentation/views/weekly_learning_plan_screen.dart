import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class WeeklyLearningPlanScreen extends StatelessWidget {
  const WeeklyLearningPlanScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Weekly Learning Plan Roadmap')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              title: Text('Monday: Array Memory Layout & Contiguity', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Focus: Resolving offset calculation misconception', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
          SizedBox(height: 12),
          AppCard(
            child: ListTile(
              title: Text('Tuesday: Array Stride Pointer Math Practice', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Focus: 5 Adaptive practice questions under Apply level', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
          SizedBox(height: 12),
          AppCard(
            child: ListTile(
              title: Text('Wednesday: Spaced Revision - BST Traversals', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Focus: Decay recovery & retention verification', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
