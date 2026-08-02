import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class PredictionDashboardScreen extends StatelessWidget {
  const PredictionDashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Predictive Analytics & Exam Readiness')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.psychology_outlined, color: AppColors.accentCyan, size: 36),
              title: Text('Exam Readiness Index: 82.0%', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Risk of Failure: 10% (Low) • Expected 8-Day Mastery: 90.0% • Intervention: None Needed', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
