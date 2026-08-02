import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class InterventionCenterScreen extends StatelessWidget {
  const InterventionCenterScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('High-Risk Student Intervention Center')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.error_outline_rounded, color: AppColors.error, size: 36),
              title: Text('Jordan Lee (Critical Failure Risk)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Reason: Persistent Stride Calculation Misconception & 35% Knowledge Decay.\nRecommended Action: 5-minute interactive offset visualizer set.', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
