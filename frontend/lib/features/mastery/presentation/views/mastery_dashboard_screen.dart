import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class MasteryDashboardScreen extends StatelessWidget {
  const MasteryDashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Mastery Intelligence Dashboard')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Text('Mastery Analytics Overview', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16)),
                Divider(color: AppColors.darkBorder),
                SizedBox(height: 8),
                Text('• Mastered Concepts: 1 of 4 (25%)', style: TextStyle(color: AppColors.success)),
                Text('• Concepts in Progress: 3 of 4 (75%)', style: TextStyle(color: AppColors.warning)),
                Text('• Bayesian Knowledge Probability (P_know Avg): 0.64', style: TextStyle(color: AppColors.accentCyan)),
                Text('• Student Learning Streak: 7 Days', style: TextStyle(color: AppColors.accentTeal)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
