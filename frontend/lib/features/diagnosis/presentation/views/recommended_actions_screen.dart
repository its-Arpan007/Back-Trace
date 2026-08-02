import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class RecommendedActionsScreen extends StatelessWidget {
  const RecommendedActionsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Recommended Actions')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.school_outlined, color: AppColors.accentTeal),
              title: Text('Action 1: Review Interactive Pointer Offset Tutorial', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Estimated Time: 10 mins • Priority: High', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
          SizedBox(height: 12),
          AppCard(
            child: ListTile(
              leading: Icon(Icons.refresh_rounded, color: AppColors.accentCyan),
              title: Text('Action 2: Attempt Targeted Pointer Arithmetic Retest', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Estimated Time: 5 mins • Priority: High', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
