import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class RetentionDashboardScreen extends StatelessWidget {
  const RetentionDashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Knowledge Retention Dashboard')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.timer_outlined, color: AppColors.accentCyan, size: 36),
              title: Text('Ebbinghaus Retention Score: 88%', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Half-Life: 14.0 Days • Next Scheduled Review: In 5 Days', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
