import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class PerformanceReportsScreen extends StatelessWidget {
  const PerformanceReportsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('PDF-Ready Performance Reports')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.picture_as_pdf_rounded, color: AppColors.accentTeal),
              title: Text('Weekly Student Learning Performance Report', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Status: Ready for PDF Export • Executive Summary: +1.45x Learning Velocity', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
