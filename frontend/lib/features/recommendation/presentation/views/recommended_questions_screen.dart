import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class RecommendedQuestionsScreen extends StatelessWidget {
  const RecommendedQuestionsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Recommended Diagnostic Questions')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.help_outline_rounded, color: AppColors.accentCyan),
              title: Text('Q: Array Stride Index 10 Address Calculation', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Difficulty: Medium • Bloom Level: Apply • Targets: DSA_ARRAYS_01', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
