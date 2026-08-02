import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class MisconceptionViewerScreen extends StatelessWidget {
  const MisconceptionViewerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Detected Misconception Library')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.bug_report_outlined, color: AppColors.error),
              title: Text('MIS_OFFSET_01: Stride Multiplication Mismatch', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Severity: High • Trigger: Provided 0x1005 (Base + Index) instead of Base + (Index * Stride)', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
