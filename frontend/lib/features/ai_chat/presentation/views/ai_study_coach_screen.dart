import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AIStudyCoachScreen extends StatelessWidget {
  const AIStudyCoachScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('AI Study Coach')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.psychology_rounded, color: AppColors.accentTeal, size: 36),
              title: Text('Personalized Pedagogical Guidance', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Grounded in your Bayesian Knowledge State and Rule Engine Diagnoses.', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
