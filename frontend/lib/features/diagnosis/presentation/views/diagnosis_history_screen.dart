import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class DiagnosisHistoryScreen extends StatelessWidget {
  const DiagnosisHistoryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Student Diagnosis Audit History')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.analytics_outlined, color: AppColors.error),
              title: Text('Diagnosis #1042 — Concept Gap', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Concept: DSA_ARRAYS_01 • Confidence: 91.5% • Severity: High • Time: 142ms', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
