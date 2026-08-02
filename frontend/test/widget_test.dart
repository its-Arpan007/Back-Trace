import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/features/student_dashboard/presentation/views/student_home_dashboard_screen.dart';

void main() {
  testWidgets('StudentHomeDashboardScreen renders properly', (WidgetTester tester) async {
    await tester.pumpWidget(
      const ProviderScope(
        child: MaterialApp(
          home: StudentHomeDashboardScreen(),
        ),
      ),
    );

    expect(find.textContaining('Welcome back'), findsOneWidget);
    expect(find.text("TODAY'S ADAPTIVE LEARNING PLAN"), findsOneWidget);
  });
}
