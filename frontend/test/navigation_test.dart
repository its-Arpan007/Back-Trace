import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:backtrace/routes/app_router.dart';

void main() {
  testWidgets('Router initializes at splash screen', (WidgetTester tester) async {
    await tester.pumpWidget(
      ProviderScope(
        child: MaterialApp.router(
          routerConfig: appRouter,
        ),
      ),
    );

    expect(find.text('BACKTRACE'), findsWidgets);
  });
}
