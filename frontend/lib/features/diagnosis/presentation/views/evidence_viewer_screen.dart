import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class EvidenceViewerScreen extends StatelessWidget {
  const EvidenceViewerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Diagnostic Evidence Records')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.assignment_turned_in_outlined, color: AppColors.error),
              title: Text('Current Submission Evidence (Weight 1.0)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Submitted answer \'0x1005\' mismatched expected \'0x1014\'.', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
          SizedBox(height: 12),
          AppCard(
            child: ListTile(
              leading: Icon(Icons.timer_outlined, color: AppColors.accentTeal),
              title: Text('Time Analysis Evidence (Weight 0.75)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Answer submitted in 45s (estimated 120s), indicating potential rushing or memory calculation error.', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
