import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class QuestionStatisticsScreen extends StatelessWidget {
  const QuestionStatisticsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Question Intelligence Analytics')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('Array Index Offset Calculation (q1_arrays_01)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16)),
                const Divider(color: AppColors.darkBorder),
                const SizedBox(height: 8),
                _buildStatRow('Total Attempts', '142 attempts'),
                _buildStatRow('Correct Accuracy Rate', '68.5%'),
                _buildStatRow('Average Solve Time', '104 seconds'),
                _buildStatRow('Hint Usage Rate', '22.4%'),
                _buildStatRow('Top Misconception Triggered', 'MIS_OFFSET_01 (45%)'),
                _buildStatRow('Top Diagnosed Root Cause', 'Concept Gap (60%)'),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildStatRow(String label, String val) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(label, style: const TextStyle(color: AppColors.textSecondaryDark)),
          Text(val, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w600)),
        ],
      ),
    );
  }
}
